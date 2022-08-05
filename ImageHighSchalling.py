from PIL import Image

i = Image.open('bene.png')
i_r = i.resize((1920, 1080), Image.Resampling.LANCZOS)
i_r.save('bene2.png', 'PNG')