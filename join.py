
import os
import zipfile
def join(files, dest_file):
    output_file = open(dest_file, 'wb')
    for file in files:
        print('Joining',file,'...')
        input_file = open(file, 'rb')
        while True:
            byte = input_file.read(100000)
            if not byte:
                break
            output_file.write(byte)
        input_file.close()
    output_file.close()
    for file in files:
        print('Removing',file,'...')
        os.remove(file)
join(['gwofl.zip.000.NOTES', 'gwofl.zip.001.NOTES', 'gwofl.zip.002.NOTES', 'gwofl.zip.003.NOTES', 'gwofl.zip.004.NOTES', 'gwofl.zip.005.NOTES', 'gwofl.zip.006.NOTES', 'gwofl.zip.007.NOTES', 'gwofl.zip.008.NOTES', 'gwofl.zip.009.NOTES', 'gwofl.zip.010.NOTES', 'gwofl.zip.011.NOTES', 'gwofl.zip.012.NOTES', 'gwofl.zip.013.NOTES', 'gwofl.zip.014.NOTES', 'gwofl.zip.015.NOTES', 'gwofl.zip.016.NOTES', 'gwofl.zip.017.NOTES', 'gwofl.zip.018.NOTES', 'gwofl.zip.019.NOTES', 'gwofl.zip.020.NOTES', 'gwofl.zip.021.NOTES', 'gwofl.zip.022.NOTES', 'gwofl.zip.023.NOTES', 'gwofl.zip.024.NOTES', 'gwofl.zip.025.NOTES', 'gwofl.zip.026.NOTES', 'gwofl.zip.027.NOTES', 'gwofl.zip.028.NOTES', 'gwofl.zip.029.NOTES', 'gwofl.zip.030.NOTES', 'gwofl.zip.031.NOTES', 'gwofl.zip.032.NOTES', 'gwofl.zip.033.NOTES', 'gwofl.zip.034.NOTES', 'gwofl.zip.035.NOTES', 'gwofl.zip.036.NOTES', 'gwofl.zip.037.NOTES', 'gwofl.zip.038.NOTES', 'gwofl.zip.039.NOTES', 'gwofl.zip.040.NOTES', 'gwofl.zip.041.NOTES', 'gwofl.zip.042.NOTES', 'gwofl.zip.043.NOTES', 'gwofl.zip.044.NOTES', 'gwofl.zip.045.NOTES', 'gwofl.zip.046.NOTES', 'gwofl.zip.047.NOTES', 'gwofl.zip.048.NOTES', 'gwofl.zip.049.NOTES', 'gwofl.zip.050.NOTES', 'gwofl.zip.051.NOTES', 'gwofl.zip.052.NOTES', 'gwofl.zip.053.NOTES', 'gwofl.zip.054.NOTES', 'gwofl.zip.055.NOTES', 'gwofl.zip.056.NOTES', 'gwofl.zip.057.NOTES', 'gwofl.zip.058.NOTES', 'gwofl.zip.059.NOTES', 'gwofl.zip.060.NOTES', 'gwofl.zip.061.NOTES', 'gwofl.zip.062.NOTES', 'gwofl.zip.063.NOTES', 'gwofl.zip.064.NOTES', 'gwofl.zip.065.NOTES', 'gwofl.zip.066.NOTES'],'gwofl.zip')
print('unziping')
with zipfile.ZipFile('gwofl.zip', 'r') as zip_ref:
    zip_ref.extractall('gwofl')
os.remove('gwofl.zip')
os.remove('join.py')
