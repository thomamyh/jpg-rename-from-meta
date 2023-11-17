from PIL import Image, ExifTags
import os
import random

def main():
    folder = input("Folder where the images are located: ")
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

    for file in files:
        rand_hex = hex(random.randint(4096, 65535))
        if "jpg" in file.lower() or "jpeg" in file.lower():
            img = Image.open(os.path.join(folder, file))
            exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
            img.close()
            time_and_date = exif['DateTime'].split(' ')
            date = time_and_date[0].replace(':', '')
            time = time_and_date[1].replace(':', '')
            new_name = f"{date}_{time}_{rand_hex[-4:]}.jpg"
            os.rename(os.path.join(folder, file), os.path.join(folder, new_name))
            print(f"Renamed {file} to {new_name}")

if __name__ == "__main__":
    main()




















    # if "mov" in file.lower() or "mp4" in file.lower():
    #     tid_og_dato = os.path.getmtime(os.path.join(folder, file))
    #     tid_og_dato = datetime.fromtimestamp(tid_og_dato).strftime('%Y%m%d %H%M%S')
    #     #print(f"{tid_og_dato}")
    #     print(file)
    #     dato = tid_og_dato.split(' ')[0]
    #     tid = tid_og_dato.split(' ')[1]
    #     nyttnavn = f"{dato}_{tid}_{file}"
    #     #print(nyttnavn)
    #     #os.rename(os.path.join(folder, file), os.path.join(folder, nyttnavn))

# for file in files:
#     if "jpg" in file.lower() or "jpeg" in file.lower():
#         try:
#             exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
#             img = Image.open(os.path.join(folder, file))
#             img.close()
#             # pprint.pprint(exif)
#             #print(f"{file}: {exif['DateTime']}")
#             tid_og_dato = exif['DateTime'].split(' ')
#             dato = tid_og_dato[0].replace(':', '')
#             tid = tid_og_dato[1].replace(':', '')
#             nyttnavn = f"{dato}_{tid}_{file}"
#             #print(nyttnavn)
#             #os.rename(os.path.join(folder, file), os.path.join(folder, nyttnavn))
#         except:
#             print("feil: " + file)
#     if "mov" in file.lower() or "mp4" in file.lower():
#         tid_og_dato = os.path.getmtime(os.path.join(folder, file))
#         tid_og_dato = datetime.fromtimestamp(tid_og_dato).strftime('%Y%m%d %H%M%S')
#         #print(f"{tid_og_dato}")
#         dato = tid_og_dato.split(' ')[0]
#         tid = tid_og_dato.split(' ')[1]
#         nyttnavn = f"{dato}_{tid}_{file}"
#         #print(nyttnavn)
#         #os.rename(os.path.join(folder, file), os.path.join(folder, nyttnavn))