function output = bgmodel_mean (k, t, s)

%READ FOLDER
myFolder = 'C:\Users\amjad\OneDrive\Desktop\AML\Assignment_6_AML\Dataset';
%READ IMAGE 1
jpgFilename_1 = sprintf('Frame%d.jpg', 1);
fullFileName_1 = fullfile(myFolder, jpgFilename_1);
imagedata_1 = imread(fullFileName_1);

%SET BG MODEL TO ZEROS SIZE OF IMAGE 1
bg_model = zeros(size(imagedata_1), class(imagedata_1));

x = zeros(size(imagedata_1), class(imagedata_1));

for m = 1:k
    jpgFilename = sprintf('Frame%d.jpg', m);
    fullFileName = fullfile(myFolder, jpgFilename);
    if exist(fullFileName, 'file')
       imagedata = imread(fullFileName);
       x = cat(3,imagedata,x);
%        N = 0;
%        avg = 0;
%       for i=1:size(imagedata,1)
%           for j=1:size(imagedata,2)
%               N = N+1;
%               a = 1/N;
%               b = 1 - a;
%               avg = a * imagedata(i,j) + b * avg;
%               bg_model(i,j) = avg;
%           end
%       end
  else
    warningMessage = sprintf('Warning: image file does not exist:\n%s', fullFileName);
    uiwait(warndlg(warningMessage));
    end

end
bg_model = mean(x,3);

jpgFilename_k1 = sprintf('Frame%d.jpg', 148);
fullFileName_k1 = fullfile(myFolder, jpgFilename_k1);
imagedata_k1 = imread(fullFileName_k1);

output = zeros(size(imagedata), class(imagedata));

for i=1:size(output,1)
    for j=1:size(output,2)
        dummy = abs(bg_model(i,j) - imagedata_k1(i,j));
        if dummy > t
            output(i,j) = 1;
        else
            output(i,j) = 0;
        end
    end
end
output = imopen(output, ones(s,s));
output = imclose(output, ones(s,s));
output = imbinarize(output);

bg_model = mat2gray(bg_model);
subplot(1,2,1);
imshow(bg_model);
title('Background Model by Mean Filtering');
subplot(1,2,2);
imshow(output);
title('Differencing image K=100, T=5, S=3');

end