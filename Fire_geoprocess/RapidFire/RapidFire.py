#this includes the package from: http://code.google.com/p/pyodbc/downloads/detail?name=pyodbc-2.1.8.win32-py2.6.exe
#This incclude the package from: http://www.stickpeople.com/projects/python/win-psycopg/ used for binding to postgres
import arcpy
from arcpy import env
#import pyodbc
import os
import os.path
import psycopg2

SQLString=''

#Define the fire points
RapidFirePointsName='FIREPOINTS'
RapdiFirePointsLocation='PATH TO DATA/SERVIR/SampleData/FIRE.gdb/'

#Define the GAUL Boundaries
BoundaryName='g2006_2'
BoundaryLocation='PATH TO BOUNDARIES/SERVIR/SampleData/GAUL_LEVELS.gdb/'
#global postgresconnection

#scratch output stuff
ScratchOutput='C:/Projects/SERVIR/SCRATCH/TEMP_OUT.gdb/tempfire'
#Spatial Join Operation
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "FIREPOINTS", "g2006_2"
#obviously all this stuff will have to change depending on the final schema
if arcpy.Exists(ScratchOutput):
    arcpy.Delete_management(ScratchOutput)

arcpy.SpatialJoin_analysis(RapdiFirePointsLocation+RapidFirePointsName,BoundaryLocation+BoundaryName,ScratchOutput,"JOIN_ONE_TO_ONE","KEEP_ALL","LATITUDE /\LATITUDE/\ true true false 8 Double 0 0 ,First,#,C:/Projects/SERVIR/SampleData/FIRE.gdb/FIREPOINTS,LATITUDE,-1,-1;LONGITUDE /\LONGITUDE/\ true true false 8 Double 0 0 ,First,#,C:/Projects/SERVIR/SampleData/FIRE.gdb/FIREPOINTS,LONGITUDE,-1,-1;BRIGHTNESS /\BRIGHTNESS/\ true true false 8 Double 0 0 ,First,#,C:/Projects/SERVIR/SampleData/FIRE.gdb/FIREPOINTS,BRIGHTNESS,-1,-1;SCAN /\SCAN/\ true true false 8 Double 0 0 ,First,#,C:/Projects/SERVIR/SampleData/FIRE.gdb/FIREPOINTS,SCAN,-1,-1;TRACK /\TRACK/\ true true false 8 Double 0 0 ,First,#,C:/Projects/SERVIR/SampleData/FIRE.gdb/FIREPOINTS,TRACK,-1,-1;ACQ_DATE /\ACQ_DATE/\ true true false 8 Date 0 0 ,First,#,C:/Projects/SERVIR/SampleData/FIRE.gdb/FIREPOINTS,ACQ_DATE,-1,-1;ACQ_TIME /\ACQ_TIME/\ true true false 8 Double 0 0 ,First,#,C:/Projects/SERVIR/SampleData/FIRE.gdb/FIREPOINTS,ACQ_TIME,-1,-1;SATELLITE /\SATELLITE/\ true true false 254 Text 0 0 ,First,#,C:/Projects/SERVIR/SampleData/FIRE.gdb/FIREPOINTS,SATELLITE,-1,-1;CONFIDENCE /\CONFIDENCE/\ true true false 8 Double 0 0 ,First,#,C:/Projects/SERVIR/SampleData/FIRE.gdb/FIREPOINTS,CONFIDENCE,-1,-1;VERSION /\VERSION/\ true true false 8 Double 0 0 ,First,#,C:/Projects/SERVIR/SampleData/FIRE.gdb/FIREPOINTS,VERSION,-1,-1;BRIGHT_T31 /\BRIGHT_T31/\ true true false 8 Double 0 0 ,First,#,C:/Projects/SERVIR/SampleData/FIRE.gdb/FIREPOINTS,BRIGHT_T31,-1,-1;FRP /\FRP/\ true true false 8 Double 0 0 ,First,#,C:/Projects/SERVIR/SampleData/FIRE.gdb/FIREPOINTS,FRP,-1,-1;WardNumber /\WardNumber/\ true true false 4 Long 0 0 ,First,#,C:/Projects/SERVIR/SampleData/FIRE.gdb/FIREPOINTS,WardNumber,-1,-1;DISTRICT /\DISTRICT/\ true true false 50 Text 0 0 ,First,#,C:/Projects/SERVIR/SampleData/FIRE.gdb/FIREPOINTS,DISTRICT,-1,-1;ZONE /\ZONE/\ true true false 50 Text 0 0 ,First,#,C:/Projects/SERVIR/SampleData/FIRE.gdb/FIREPOINTS,ZONE,-1,-1;VDC /\VDC/\ true true false 50 Text 0 0 ,First,#,C:/Projects/SERVIR/SampleData/FIRE.gdb/FIREPOINTS,VDC,-1,-1;NEAR_FID /\NEAR_FID/\ true true false 4 Long 0 0 ,First,#,C:/Projects/SERVIR/SampleData/FIRE.gdb/FIREPOINTS,NEAR_FID,-1,-1;NEAR_DIST /\NEAR_DIST/\ true true false 8 Double 0 0 ,First,#,C:/Projects/SERVIR/SampleData/FIRE.gdb/FIREPOINTS,NEAR_DIST,-1,-1;ADM2_CODE /\ADM2_CODE/\ true true false 8 Double 0 0 ,First,#,C:/Projects/SERVIR/SampleData/GAUL_LEVELS.gdb/g2006_2,ADM2_CODE,-1,-1;ADM0_CODE /\ADM0_CODE/\ true true false 8 Double 0 0 ,First,#,C:/Projects/SERVIR/SampleData/GAUL_LEVELS.gdb/g2006_2,ADM0_CODE,-1,-1;ADM0_NAME /\ADM0_NAME/\ true true false 100 Text 0 0 ,First,#,C:/Projects/SERVIR/SampleData/GAUL_LEVELS.gdb/g2006_2,ADM0_NAME,-1,-1;ADM1_NAME /\ADM1_NAME/\ true true false 100 Text 0 0 ,First,#,C:/Projects/SERVIR/SampleData/GAUL_LEVELS.gdb/g2006_2,ADM1_NAME,-1,-1;ADM1_CODE /\ADM1_CODE/\ true true false 8 Double 0 0 ,First,#,C:/Projects/SERVIR/SampleData/GAUL_LEVELS.gdb/g2006_2,ADM1_CODE,-1,-1;ADM2_NAME /\ADM2_NAME/\ true true false 100 Text 0 0 ,First,#,C:/Projects/SERVIR/SampleData/GAUL_LEVELS.gdb/g2006_2,ADM2_NAME,-1,-1;REGION /\REGION/\ true true false 150 Text 0 0 ,First,#,C:/Projects/SERVIR/SampleData/GAUL_LEVELS.gdb/g2006_2,REGION,-1,-1","INTERSECT","#","#")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "FIREPOINTS", "g2006_2"
rows = arcpy.UpdateCursor(ScratchOutput) 
fields = arcpy.ListFields(ScratchOutput , "", "ALL")
for row in rows:
        #for field in fields:
        #print row.getValue('LATITUDE') 
        #print row.getValue('LONGITUDE') 
        #print row.getValue('WardNumber') 
                    #print str(row.getValue)
        SQLString+='insert into fire_bump_output (x, y, regionid) VALUES ('+str(row.getValue('LONGITUDE'))+','+str(row.getValue('LATITUDE'))+','+str(row.getValue('WardNumber'))+'); '
#for field in fieldList        
        #print SQLString
    
#    print ("%s is a type of %s with a length of %i" % (field.name, field.type, field.length) )
print SQLString
conn = psycopg2.connect("dbname=DB NAME user=DB USER password=DB PASSWORD host=DB HOST IP port=5432")
cur = conn.cursor()
cur.execute(SQLString)
conn.commit()


print cur.rowcount

#insert into fire_bump_output (x, y, regionid) VALUES (-122.34343,55.54545,5);

cur.close()
conn.close()