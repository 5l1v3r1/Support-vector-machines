Sayın Ercan Hocam,

Projeyi yaparken Asife destek olup yol gösterip olayı kavramasını sağlamak adına kodlarımı onunla belli oranda paylaştım.
( Dosyaların okunması, Datasetlerin train test olarak ayrıştırılması, ve temel svm ve kfold kısmı ).

Devamında ise ona sadece izlemesi gerekn adımları belirtip başka bir destekte bulunmadım.
( C ve Y değerlerini bir matriste tutması gerektiğini , bu ikilileri train setiyle train etmesi gerektiğini for ile bunu yapması gerektiğini ve bulduğu en iyi 2 liyi test sette train etmesi gerektiğini vs sadece sözlü olarak illettim)

Ayrıca kendi kodum için

Proje çalıştırıldığında 2 cellde uyarı alıyor :

C:\Users\user\Anaconda3\lib\site-packages\sklearn\utils\validation.py:724: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().
  y = column_or_1d(y, warn=True)

Ama uyarı kodun çalışmasını engellememekte. ( daha öncesinde y_train ve y_test 'e .ravel() ekleyerek çözmüştüm am abu sefer nedense olmadı )

Saygılarımla,
Berkay Can Özçelik