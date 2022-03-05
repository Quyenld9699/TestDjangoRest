# TestDjangoRest

## Tutorial

[https://www.youtube.com/playlist?list=PLo7TNe_pEoMXcsc1dOaFyVGcZK8o-6CCW](https://www.youtube.com/playlist?list=PLo7TNe_pEoMXcsc1dOaFyVGcZK8o-6CCW)

## Hoc ve Models

![code example](./img/codeModels.png)

```
    Hoc ve Models
    - cac loai Field co trong django rest
    - def __str__(self): | => format hien thi object tren admin page
    - class Meta: | => them chuc nang sap xep object theo Field, chinh name hien thi cua Model
    - def save(self, *args, **kwargs): | => action while save data in db
```

![code example](./img/codeModels2.png)

```
    - ForeignKey chu y: co cac kieu on_delete khac nhau
```

![code example](./img/codeModels3.png)

```
    - OneToOneField chu y: co cac kieu on_delete khac nhau, quan he 1-1
```

## Hoc ve Views

![code example](./img/codeViews1.png)
`tao mot api request don gian`

![code example](./img/codeViews2.png)

```
    dung APIView: khong co serializer: postMethod phai tao chay nhu tren
```

![code example](./img/codeViews3.png)

```
    dung APIView: co su dung serializer: postMethod ngan gon
```

## Hoc Serializers

![code example](./img/codeSerializer1.png)

```
    dung serializer.Serializer :
    - phai viet ham create, update de khi post va put .save() map voi funtion tren
```

![code example](./img/codeSerializer2.png)

```
    su dung ModalSerializer: duoc ho tro het
```

## quay lai voi Views

![code example](./img/codeViews4.png)

```
    generics: ho tro api GET POST PUT DELETE
    Chu y: generics.UpdateAPIView tham so default la 'pk'.
    Muon thay doi phai set: lookup_field ="name_field"
```
