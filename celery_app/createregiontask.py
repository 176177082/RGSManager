#!C:/Python27/ArcGIS10.2/python.exe
# -*- coding:utf-8 -*-
import sys
import os
import arcpy
import shutil
from datetime import datetime
import psycopg2
from unrar import rarfile

from celery_app import app
from ziptools import zipUpFolder
import zipfile

reload(sys)
sys.setdefaultencoding('utf8')


@app.task
def createregiontask(regiontask_id, regiontask_filepath):

    # 解压文件
    file_dir = os.path.dirname(regiontask_filepath)
    z = zipfile.is_zipfile(regiontask_filepath)
    r = rarfile.is_rarfile(regiontask_filepath)

    if z:
        fz = zipfile.ZipFile(regiontask_filepath, 'r')
        for file in fz.namelist():
            fz.extract(file, file_dir)
        filename = regiontask_filepath.split("\\")[-1].split(".zip")[0]
        unzipfile = os.path.join(file_dir, filename)
        print unzipfile
    elif r:
        fz = rarfile.RarFile(regiontask_filepath, 'r')
        for file in fz.namelist():
            fz.extract(file, file_dir)
        filename = regiontask_filepath.split("\\")[-1].split(".rar")[0]
        unrarfile = os.path.join(file_dir, filename)
        print unrarfile
    else:
        print('This is not zip or rar')
        return False

    # 修改关系库中的数据
    tablename = u"taskpackages_regiontask"
    status = u"处理完成"
    basemapservice = u'basemapservice'
    mapindexfeatureservice = u"mapindexfeatureservice"
    mapindexmapservice = u"mapindexmapservice"
    mapindexschedulemapservice = u"mapindexschedulemapservice"


    change_db_regiontasktable(tablename, regiontask_id, status, basemapservice,
                              mapindexfeatureservice, mapindexmapservice, mapindexschedulemapservice)
    return True


def change_db_regiontasktable(tablename, regiontask_id, status, basemapservice,
                              mapindexfeatureservice, mapindexmapservice, mapindexschedulemapservice):
    conn = psycopg2.connect(dbname=u"mmanageV8.0",
                            user=u"postgres",
                            password=u"Lantucx2018",
                            host=u"localhost",
                            port=u"5432")
    cur = conn.cursor()
    UPDATESQL = u"update %s set status='%s',basemapservice='%s',mapindexfeatureservice='%s',mapindexmapservice='%s',mapindexschedulemapservice='%s' where ID=%d" % (
        tablename, status, basemapservice, mapindexfeatureservice, mapindexmapservice, mapindexschedulemapservice,regiontask_id)
    cur.execute(UPDATESQL)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    id14 = u"D:\\code\\RGSManager\\media\\data\\2019\\02\\14\\2019-02-14-14-29-34-035000\\gb.gdb.zip"
    id15 = u"D:\\code\\RGSManager\\media\\data\\2019\\02\\14\\2019-02-14-14-30-05-055000\\gb.gdb.rar"

    # createregiontask(14, id14)
    createregiontask(15, id15)
