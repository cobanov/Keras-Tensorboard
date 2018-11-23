# Keras-Tensorboard

Bu repo tensorboard özelliklerini keras ile kullanmak için örnek çalışmalar içerir.

## Kullanım:
Gerekli kütüphaneler kurulduğunda komut satırı üzerinden `python kerasboard.py` komutu ile çalıştırılabilir.

Model eğitimi tamamlandıktan sonra programın son çıktısı komut satırında çalıştırılarak tarayıcıda `localhost:6006` adresine gidilerek grafikler gözlenebilir.

## Nedir:
Oluşturulan bir yapay sinir ağında elde edilen parametreleri ve katmanların incelenmesi için kullanılan tensorboard'un keras ile nasıl çalıştırılacağı adına örnek bir proje.

## Model:
* Data: MNIST
* Tür: Konvolüsyonel Sinir Ağı
* Optimizer: Adam
* Loss: Categorical Crossentropy

## Gerekli Kütüphaneler:
* Tensorflow
* Keras

## Olası Hatalar:
Path error alındığı takdirde, C: dizini altında *tmp* adlı klasör oluşturun.