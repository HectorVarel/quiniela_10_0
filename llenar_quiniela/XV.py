import os
from moviepy.editor import ImageClip, concatenate_videoclips
from moviepy.video.fx.all import fadein, fadeout, resize

# Función para aplicar transiciones variadas entre clips
def apply_transition(clip1, clip2, effect):
    if effect == "fade":
        return clip1.crossfadein(1).set_start(clip1.duration - 1).crossfadeout(1)
    elif effect == "fadein":
        return fadein(clip2, 1)
    elif effect == "fadeout":
        return fadeout(clip1, 1)
    else:
        return clip1.set_duration(clip1.duration + 1).set_end(clip1.duration + 1)

# Directorio que contiene las imágenes
image_dir = "E:/Fotos"

# Obtener una lista de archivos de imagen en el directorio
image_files = [os.path.join(image_dir, f) for f in sorted(os.listdir(image_dir)) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Crear una lista de ImageClips
clips = [ImageClip(img).set_duration(2).resize(height=720) for img in image_files]

# Crear una lista para los clips con transiciones
clips_with_transitions = []

# Efectos de transición a aplicar
effects = ["fade", "fadein", "fadeout"]

# Añadir clips con transiciones
for i in range(len(clips) - 1):
    clip_with_transition = apply_transition(clips[i], clips[i+1], effects[i % len(effects)])
    clips_with_transitions.append(clip_with_transition)

# Añadir el último clip sin transición
clips_with_transitions.append(clips[-1])

# Concatenar todos los clips
final_video = concatenate_videoclips(clips_with_transitions, method="compose")

# Escribir el video final en un archivo
final_video.write_videofile("C:/Users/varel/Videos/video.mp4", fps=24)


