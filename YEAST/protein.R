setwd("D:/R/bioinformatics")
setwd("D:/nyu课件/第二学期/bioinformatics/biodata/YEAST")

#data=read.table("clean.txt",header=T,sep="\t")
data=read.table("ProteinNormalized_Diam.txt",header=T,sep="\t",quote = '"')
rownames(data)=data[,1]
mydata=data[,-1]

# Determine number of clusters
wss <- (nrow(mydata)-1)*sum(apply(mydata,2,var))
for (i in 2:15) wss[i] <- sum(kmeans(mydata, centers=i)$withinss)

plot(1:15, wss, type="b", xlab="Number of Clusters",ylab="Within groups sum of squares")

# K-Means Cluster Analysis
fit <- kmeans(mydata, 6) # 6 cluster solution

aggregate(mydata,by=list(fit$cluster),FUN=mean)
mydata <- data.frame(mydata, fit$cluster)

write.table(x = mydata, file = "protein.txt",sep ="\t",row.names = T,quote = F)

library(cluster) 
clusplot(mydata, fit$cluster, color=TRUE, shade=F, labels=1, lines=0,col.p = fit$cluster, col.clus = c("#999999","#1B75BB","#37B34A","#000000"),plotchar = F,cex = 1.5,pch=16)


