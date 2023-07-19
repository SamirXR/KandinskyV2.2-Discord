class auth:
    DISCORD = ""
  

class names:
    sd14 = "sdv1_4.ckpt [7460a6fa]"
    sd15 = "v1-5-pruned-emaonly.ckpt [81761151]"
    anyv3 = "anythingv3_0-pruned.ckpt [2700c435]"
    anyv4 = "anything-v4.5-pruned.ckpt [65745d25]"
    anyv5 = "anythingV5_PrtRE.safetensors [893e49b9]"
    orangemix = "AOM3A3_orangemixs.safetensors [9600da17]"
    analog = "analog-diffusion-1.0.ckpt [9ca13f02]"
    theallys = "theallys-mix-ii-churned.safetensors [5d9225a4]"
    evm = "elldreths-vivid-mix.safetensors [342d9d26]"
    deliberate = "deliberate_v2.safetensors [10ec4b29]"
    openjourney = "openjourney_V4.ckpt [ca2f377f]"
    dreaml1 = "dreamlike-diffusion-1.0.safetensors [5c9fd6e0]"
    dreaml2 = "dreamlike-diffusion-2.0.safetensors [fdcf65e7]"
    portrait = "portrait+1.0.safetensors [1400e684]"
    riffusion = "riffusion-model-v1.ckpt [3aafa6fe]"
    timeless = "timeless-1.0.ckpt [7c4971d4]"
    dreamshaper5 = "dreamshaper_5BakedVae.safetensors [a3fbf318]"
    dreamshaper6 = "dreamshaper_6BakedVae.safetensors [114c8abb]"
    sbp = "shoninsBeautiful_v10.safetensors [25d8c546]"
    rev = "revAnimated_v122.safetensors [3f4fefd9]"
    meina = "meinamix_meinaV9.safetensors [2ec66ab0]"
    lyriel15 = "lyriel_v15.safetensors [65d547c5]"
    lyriel16 = "lyriel_v16.safetensors [68fceea2]"
    realisticvs20 = "Realistic_Vision_V2.0.safetensors [79587710]"
    realisticvs14 = "Realistic_Vision_V1.4-pruned-fp16.safetensors [8d21810b]"
    modellist = [
    "SD v1.4",
    "SD v1.5",
    "Anything v3",
    "Anything v4",
    "Anything v5",
    "AbyssOrangeMix v3",
    "Analog v1",
    "TheAlly's Mix II",
    "Elldreth's Vivid",
    "Deliberate v2",
    "Openjourney v4",
    "Dreamlike Diffusion v1",
    "Dreamlike Diffusion v2",
    "Portrait v1",
    "Timeless v1",
    "Riffusion v1"
    "DreamShaper v5",
    "DreamShaper v6",
    "revAnimated v1.2.2",
    "MeinaMix v9",
    "Lyriel v1.5",
    "Lyriel v1.6",
    "Realistic Vision v1.4",
    "Realistic Vision v2.0",
    "Shonin's Beautiful People"
]
    samplerlist = ["Euler", "Euler a", "Heun", "DPM++ 2M Karras", "DDIM"]
    stylelist = [
        "none",
        "anime",
        "cyberpunk",
        "detailed",
        "medieval",
        "christmas",
        "portrait",
        "professional_studio",
        "high_quality_art",
        "3d_render",
        "soviet_cartoon",
        "cartoon",
        "pencil_drawing",
        "mosaic",
        "christian_icon",
        "oil_painting",
        "renaissance",
        "classicism",
        "khokhloma",
        "picasso",
        "gonharova",
        "malevich",
        "aivazovsky",
        "kandinsky"
    ]

def fetch_model(model_name):
    if model_name == "SD v1.4":
        model = names.sd14
    elif model_name == "SD v1.5":
        model = names.sd15
    elif model_name == "Anything v3":
        model = names.anyv3
    elif model_name == "Anything v4":
        model = names.anyv4
    elif model_name == "Anything v5":
        model = names.anyv5
    elif model_name == "AbyssOrangeMix v3":
        model = names.orangemix
    elif model_name == "Analog v1":
        model = names.analog
    elif model_name == "TheAlly's Mix II":
        model = names.theallys
    elif model_name == "Elldreth's Vivid":
        model = names.evm
    elif model_name == "Deliberate v2":
        model = names.deliberate
    elif model_name == "Openjourney v4":
        model = names.openjourney
    elif model_name == "Dreamlike Diffusion v1":
        model = names.dreaml1
    elif model_name == "Dreamlike Diffusion v2":
        model = names.dreaml2
    elif model_name == "Portrait v1":
        model = names.portrait
    elif model_name == "Timeless v1":
        model = names.timeless
    elif model_name == "DreamShaper v5":
        model = names.dreamshaper5
    elif model_name == "DreamShaper v6":
        model = names.dreamshaper6
    elif model_name == "revAnimated v1.2.2":
        model = names.rev
    elif model_name == "MeinaMix v9":
        model = names.meina
    elif model_name == "Lyriel v1.5":
        model = names.lyriel15
    elif model_name == "Lyriel v1.6":
        model = names.lyriel16
    elif model_name == "Realistic Vision v1.4":
        model = names.realisticvs14
    elif model_name == "Realistic Vision v2.0":
        model = names.realisticvs20
    elif model_name == "Shonin's Beautiful People":
        model = names.sbp
    elif model_name == "Riffusion v1":
        model = names.riffusion
    else:
        model = names.realisticvs14
    return model
