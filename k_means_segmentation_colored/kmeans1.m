x=[1 1;1 2;2 1;10 10;10 11;11 10];

IDX = kmeans(x, 3);

gscatter(x(:,1),x(:,2),IDX)
legend('Cluster 1','Cluster 2')