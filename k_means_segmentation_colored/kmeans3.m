image = imread('Objects.bmp');
[idx, c, sumd] = kmeans(image, k);
for index=1:K
    numerator = c(index) - (sumd(index));
    ssd = sum(numerator(:).^2);
    numerator = (1/numel(idx)) * ssd; 
end
M = (1/K) * numerator;
sum2 = 0;
for index=1:K
    sum2 = sum2 + c(index);
end
denominator = sum2/K;
N = (2/K *(K-1)) * denominator;
Q = M / N;