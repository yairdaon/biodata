setwd("D:/R/bioinformatics")

data=read.table("clean.txt",header=T,sep="\t")
rn=data[,1]
mydata=data[,-1]

# Determine number of clusters
wss <- (nrow(mydata)-1)*sum(apply(mydata,2,var))
for (i in 2:15) wss[i] <- sum(kmeans(mydata, centers=i)$withinss)

plot(1:15, wss, type="b", xlab="Number of Clusters",ylab="Within groups sum of squares")

# K-Means Cluster Analysis
fit <- kmeans(mydata, 5) # 5 cluster solution

aggregate(mydata,by=list(fit$cluster),FUN=mean)
mydata <- data.frame(mydata, fit$cluster)

mydata=data.frame(Genenames=rn, mydata)

write.table(x = mydata, file = "cluster.txt",sep ="\t",row.names = F,quote = F)
