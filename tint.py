#### THE BELOW CODE IS COPY PASTED CODE FROM https://stackoverflow.com/questions/29332424/changing-colour-of-an-image/29379704#29379704 

from PIL import Image
from PIL.ImageColor import getcolor, getrgb
from PIL.ImageOps import grayscale

def image_tint(src, tint='#ffffff'):
    src = Image.open(src)
    if src.mode not in ['RGB', 'RGBA']:
        raise TypeError('Unsupported source image mode: {}'.format(src.mode))
    src.load()

    tr, tg, tb = getrgb(tint)
    tl = getcolor(tint, "L")  # tint color's overall luminosity
    if not tl: tl = 1  # avoid division by zero
    tl = float(tl)  # compute luminosity preserving tint factors
    sr, sg, sb = map(lambda tv: tv/tl, (tr, tg, tb))  # per component
                                                      # adjustments
    # create look-up tables to map luminosity to adjusted tint
    # (using floating-point math only to compute table)
    luts = (tuple(map(lambda lr: int(lr*sr + 0.5), range(256))) +
            tuple(map(lambda lg: int(lg*sg + 0.5), range(256))) +
            tuple(map(lambda lb: int(lb*sb + 0.5), range(256))))
    l = grayscale(src)  # 8-bit luminosity version of whole image
    if Image.getmodebands(src.mode) < 4:
        merge_args = (src.mode, (l, l, l))  # for RGB verion of grayscale
    else:  # include copy of src image's alpha layer
        a = Image.new("L", src.size)
        a.putdata(src.getdata(3))
        merge_args = (src.mode, (l, l, l, a))  # for RGBA verion of grayscale
        luts += tuple(range(256))  # for 1:1 mapping of copied alpha values

    return Image.merge(*merge_args).point(luts)

### END COPY PASTED CODE
import nextcord as discord
from urllib.request import urlopen
#from os.path import splitfile
from os.path import split
async def img_tint_main(ctx, color, url):
  ext = split(url)[-1]
  ext = ext.split(".")[-1]
  raw_imag = urlopen(url)
  if not (raw_imag.getcode() < 400): #2xx or 3xx status code = good; I don't think it will return 1xx
    await ctx.send(f"HTTP error {raw_imag.getcode()} occured while accessing the URL.")
    return "error"
  if raw_imag.info().get_content_maintype() != "image": #Ensures that the content is an image by checking MIME type
    await ctx.send(f"The link given does not go to an image; rather, it goes to content of MIME type `{raw_imag.info().get_content_type()}`")
    return "error"
  imag = image_tint(urlopen(url), color)
  return imag
