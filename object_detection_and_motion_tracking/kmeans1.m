loc1 = 255;
loc2 = 100;
loc3 = 175;
loc4 = 0;
locs = [loc1; loc2; loc3; loc4];
clusters = 4;
% [idx,C] = kmeans(image(:),clusters, 'Start',locs);
% 
% 
final = reshape(idx, size(image));
% [x,y,v] = find(final==4);
% disp(mean(x));
% disp(mean(y));
output_img = mat2gray(final);
myFolder = 'C:\Users\amjad\OneDrive\Desktop\Mini_Project_1_AML\MP1\videoFrames';
% Check to make sure that folder actually exists.  Warn user if it doesn't.
if ~isfolder(myFolder)
    errorMessage = sprintf('Error: The following folder does not exist:\n%s\nPlease specify a new folder.', myFolder);
    uiwait(warndlg(errorMessage));
    myFolder = uigetdir(); % Ask for a new one.
    if myFolder == 0
         % User clicked Cancel
         return;
    end
end
% Get a list of all files in the folder with the desired file name pattern.
filePattern = fullfile(myFolder, '*.jpg'); % Change to whatever pattern you need.
theFiles = dir(filePattern);
mean_1 = [];
mean_2 = [];
mean_3 = [];
mean_4 = [];
for i = 1 : length(theFiles)
        baseFileName = theFiles(i).name;
        fullFileName = fullfile(theFiles(i).folder, baseFileName);
        image = imread(fullFileName);
        [idx,C] = kmeans(image(:),clusters, 'Start',locs);
        final = reshape(idx, size(image));
        
    for k=1:clusters
        [x,y,v] = find(final == k);
        if(k == 1)
            mean_1 = [mean_1;mean(double(x)), mean(double(y))];
        end
        if(k == 2)
            mean_2 = [mean_2;mean(double(x)), mean(double(y))];
        end
        if(k == 3)
            mean_3 = [mean_3;mean(double(x)), mean(double(y))];
        end
        if(k == 4)
            mean_4 = [mean_4;mean(double(x)), mean(double(y))];
        end
    end
end

figure;
imshow(output_img , 'InitialMagnification', 'fit');
hold on
% scatter(mean_1(:,2), mean_1(:,1), 'rd');
% scatter(mean_2(:,2), mean_2(:,1), 'rd');
% scatter(mean_3(:,2), mean_3(:,1), 'rd');
% scatter(mean_4(:,2), mean_4(:,1), 'rd');
%disp([x,y,v]);


