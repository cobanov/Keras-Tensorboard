# Keras-Tensorboard

Bu repo tensorboard özelliklerini keras ile kullanmak için örnek çalışmalar içerir.

![Tensorboard Keras](https://media.giphy.com/media/1pA8T9iMWWnOg7Kuej/giphy.gif)

## Getting Started

Oluşturulan bir yapay sinir ağında elde edilen parametreleri ve katmanların incelenmesi için kullanılan tensorboard'un keras ile nasıl çalıştırılacağı adına örnek bir proje.

### Prerequisites

```
Python 3.x.x
TensorFlow
Keras
```

### Installing
Gerekli kütüphaneler kurulduğunda komut satırı üzerinden `python kerasboard.py` komutu ile çalıştırılabilir.

Model eğitimi tamamlandıktan sonra programın son çıktısı komut satırında çalıştırılarak tarayıcıda `localhost:6006` adresinde grafikler gözlenebilir.

![Kerasboard](https://media.giphy.com/media/7zxZ8mOddFwZvTZJoa/giphy.gif)

Ayrıca kapsamlı rehbere Deep Learning Türkiye Medium sayfasından ulaşabilirsiniz. 
[Rehber Linki](https://medium.com/deep-learning-turkiye/tensorboard-başlangıç-rehberi-198ea522b01) 

### Notes:
Path error alındığı takdirde, C: dizini altında *tmp* adlı klasör oluşturun.

## Model:
* Data: MNIST
* Tür: CNN
* Optimizer: Adam
* Loss: Categorical Crossentropy

## Authors

* **Mert Çobanoğlu** - [cobanov](https://github.com/cobanov)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


