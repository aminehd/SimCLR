import gdown
url = "https://drive.google.com/u/1/uc?id=1hcVWxD7TgfEBRof4w0cIOGNC2l_wcG58&export=download"
gdown.download(url, 'test.tar')

url = "https://drive.google.com/u/1/uc?id=1SPrSm-gSmrzzYzW75kThO9WqH9P-Akuq&export=download"
gdown.download(url, 'train.tar')

url = "https://drive.google.com/u/1/uc?id=1B9_GdxJtz1Ei8Vu2ZHf3Az-qmOOI_Xu3&export=download"
gdown.download(url, 'validation.tar')
