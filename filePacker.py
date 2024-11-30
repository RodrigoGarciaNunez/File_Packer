import os
import shutil

def packer(directory):
    
    for archivo in os.listdir(directory):
        full = os.path.join(directory, archivo)

        if os.path.isfile(full):
            
            extension = os.path.splitext(archivo)[1][1:].lower()
            
            if not extension:
                extension = "no_extension"

            new_dir = os.path.join(directory, extension)
            os.makedirs(new_dir, exist_ok=True)

            shutil.move(full, os.path.join(new_dir, archivo))
            print(f"Movido: {archivo} -> {new_dir}")
    
    

if __name__ == "__main__":
    dir = input("Write the directory that you want to organize by extension: ")
    packer(dir)
