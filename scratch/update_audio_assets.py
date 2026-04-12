import base64
import os

def get_base64_from_wav(file_path):
    with open(file_path, 'rb') as wav_file:
        return base64.b64encode(wav_file.read()).decode('utf-8')

def update_audio_assets():
    dir_path = r'c:\RitmosBR\RitmosBR'
    wav_files = ['G2.wav', 'C3.wav', 'E3.wav', 'B3.wav', 'D4.wav']
    
    output_content = "const AUDIO_ASSETS = {\n"
    
    entries = []
    for wav_name in wav_files:
        key = wav_name.split('.')[0]
        full_path = os.path.join(dir_path, wav_name)
        if os.path.exists(full_path):
            print(f"Processing {wav_name}...")
            b64_str = get_base64_from_wav(full_path)
            entries.append(f'  "{key}": "{b64_str}"')
        else:
            print(f"Warning: {wav_name} not found.")
            
    output_content += ",\n".join(entries)
    output_content += "\n};\n"
    
    with open(os.path.join(dir_path, 'audio_assets.js'), 'w') as f:
        f.write(output_content)
    
    print("audio_assets.js updated successfully!")

if __name__ == "__main__":
    update_audio_assets()
