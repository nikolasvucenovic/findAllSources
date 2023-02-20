import os
import csv

lokacije = r'U:\PRODUCTIONS\BG_MUAWIYA\sequences\115_1121'
tmpSourceLocation = []
framesArrey = []
petern = "source"
outputArrey = []
shotInfoArrey = []

# CSV 
fields = ['shotNumb', 'first frame', 'last frame']
with open('frejmoviCorrected12.csv', 'w', newline='') as f:



    for (root,dirs,files) in os.walk(lokacije):
        x = root.split('\\')
        if x[-3] == petern:
            
            tmpSourceLocation.append(root)

    # print(tmpSourceLocation)


    for path in tmpSourceLocation:
        # testPath = r"U:\PRODUCTIONS\BG_MUAWIYA\sequences\115_1121\0050\source\MW_115_11+21_0050_RAW_v001\MW_115_11+21_0050_RAW_v001"
        framesArrey.clear()
        # shotInfoArrey.clear()
        filenames = os.listdir(path)
        # print(path)
        for filename in filenames:
            
            _ = filename.split('_')
            framesArrey.append(_[-1].strip('.exr'))
            shotNumb = str(_[3])
        maxFr = str(max(framesArrey))
        minFr = str(min(framesArrey))
        print("Shot: " + shotNumb + " frames: " + minFr + " - " + maxFr)
        
        shotInfoArrey = [shotNumb,minFr,maxFr]
        
        outputArrey.append(shotInfoArrey)
        
        
        
    csv_writer = csv.writer(f)
    csv_writer.writerow(fields)
    csv_writer.writerows(shotInfoArrey)

    print(outputArrey)
        


  

  

      
    csv_writer = csv.writer(f)
    csv_writer.writerow(fields)
    csv_writer.writerows(outputArrey)

   