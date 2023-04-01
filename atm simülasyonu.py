import random
para=[]
for i in range(100):
    para += [10,20,50,100,200]
saat=8
dakika=0
sira=[1,2,3,4,5,6,7,8,9,10]
kisi=0
while True:
    for i in range(10):                
        pcy=int(random.gammavariate(2,30))*10
        p200=pcy//200
        p100=(pcy-p200*200)//100
        p50=(pcy-(p200*200+p100*100))//50
        p20=(pcy-(p200*200+p100*100+p50*50))//20
        p10=(pcy-(p200*200+p100*100+p50*50+p20*20))//10
        p1=para.count(200)
        p2=para.count(100)
        p3=para.count(50)
        p4=para.count(20)
        p5=para.count(10)
        if pcy<=sum(para) and pcy<=2000 and pcy>0:
            kisi+=1
            a=random.randint(1,15)
            dakika+=a
            if dakika>=60:
                saat+=1
                dakika=dakika-60
            rastgele=random.choice(sira)
            if rastgele==5:
                sira.remove(rastgele)
                for j in range(p200):
                    para.append(200)
                for k in range(p100):
                    para.append(100)
                for l in range(p50):
                    para.append(50)
                for m in range(p20):
                    para.append(20)
                for n in range(p10):
                    para.append(10)
                if dakika<10:
                    print(str(kisi)+". Kişi",pcy,"TL Para Yatırdı","Saat:",str(saat)+":"+"0"+str(dakika),"\nVerilen Banknotlar:","200 lük:",p200,"adet,","100 lük:",p100,"adet,","50 lik:",p50,"adet,","20 lik:",p20,"adet,","10 luk:",p10,"adet""\nKalan Banknotlar:","200 lük:",para.count(200),"adet,","100 lük:",para.count(100),"adet,","50 lik:",para.count(50),"adet,","20 lik:",para.count(20),"adet,","10 luk:",para.count(10),"adet\n")
                else:
                    print(str(kisi)+". Kişi",pcy,"TL Para Yatırdı","Saat:",str(saat)+":"+str(dakika),"\nVerilen Banknotlar:","200 lük:",p200,"adet,","100 lük:",p100,"adet,","50 lik:",p50,"adet,","20 lik:",p20,"adet,","10 luk:",p10,"adet""\nKalan Banknotlar:","200 lük:",para.count(200),"adet,","100 lük:",para.count(100),"adet,","50 lik:",para.count(50),"adet,","20 lik:",para.count(20),"adet,","10 luk:",para.count(10),"adet\n")
            else:
                sira.remove(rastgele)
                if para.count(200)>=p200:
                    for j in range(p200):
                        para.remove(200)
                else:
                    b=p200-para.count(200)
                    p100+=2*b
                    for i in range(para.count(200)):
                        para.remove(200)
                if para.count(100)>=p100:
                    for k in range(p100):
                        para.remove(100)
                else:
                    c=p100-para.count(100)
                    p50+=2*c
                    for i in range(para.count(100)):
                        para.remove(100)
                if para.count(50)>=p50:
                    for l in range(p50):
                        para.remove(50)
                else:
                    d=p50-para.count(50)
                    p20+=2*d
                    p10+=d
                    for i in range(para.count(50)):
                        para.remove(50)
                if para.count(20)>=p20:
                    for m in range(p20):
                        para.remove(20)
                else:
                    e=p20-para.count(20)
                    p10+=2*e
                    for i in range(para.count(20)):
                        para.remove(20)                           
                if para.count(10)>=p10:
                    for n in range(p10):
                        para.remove(10)
                if dakika<10:
                    print(str(kisi)+". Kişi",pcy,"TL Para Çekti","Saat:",str(saat)+":"+"0"+str(dakika),"\nÇekilen Banknotlar:","200 lük:",p1-para.count(200),"adet,","100 lük:",p2-para.count(100),"adet,","50 lik:",p3-para.count(50),"adet,","20 lik:",p4-para.count(20),"adet,","10 luk:",p5-para.count(10),"adet""\nKalan Banknotlar:","200 lük:",para.count(200),"adet,","100 lük:",para.count(100),"adet,","50 lik:",para.count(50),"adet,","20 lik:",para.count(20),"adet,","10 luk:",para.count(10),"adet\n")
                else:
                    print(str(kisi)+". Kişi",pcy,"TL Para Çekti","Saat:",str(saat)+":"+str(dakika),"\nÇekilen Banknotlar:","200 lük:",p1-para.count(200),"adet,","100 lük:",p2-para.count(100),"adet,","50 lik:",p3-para.count(50),"adet,","20 lik:",p4-para.count(20),"adet,","10 luk:",p5-para.count(10),"adet""\nKalan Banknotlar:","200 lük:",para.count(200),"adet,","100 lük:",para.count(100),"adet,","50 lik:",para.count(50),"adet,","20 lik:",para.count(20),"adet,","10 luk:",para.count(10),"adet\n")
    sira=[1,2,3,4,5,6,7,8,9,10]
    if len(para)==0:break
print("--Para Bitti--")