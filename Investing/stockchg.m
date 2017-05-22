vol=0.05; %volatility of stock (beta)
prc=778;  %current price of stock
hr=30;    %time span in days
plt=zeros(1,hr);

for x=1:hr
    fprc=prc*(1+norminv(rand(),0,vol));
    mean=fprc;
for i=1:1000
    fprc(i)=mean*(1+norminv(rand(),0,vol));
end
mean=sum(fprc)/1000;
plt(x)=mean;
prc=mean;
end

low=min(fprc)
plot(plt);
max=max(plt)
median=median(fprc)
dev=std(fprc)
