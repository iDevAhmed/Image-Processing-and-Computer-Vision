vidObj = VideoReader('Simple_bouncing_balls.mp4');
numFrames = ceil(vidObj.FrameRate*vidObj.Duration);

Folder = 'C:\Users\amjad\OneDrive\Desktop\Mini_Project_1_AML\MP1\videoFrames';

loc1 = 255;
loc2 = 100;
loc3 = 175;
loc4 = 0;
locs = [loc1; loc2; loc3; loc4];
clusters = 4;

frame_1 = readFrame(vidObj, 'native');
grey_frame1 = rgb2gray(frame_1);
n = 1;


mean_1 = [];
mean_2 = [];
mean_3 = [];
mean_4 = [];
while hasFrame(vidObj)
  frames = readFrame(vidObj, 'native');
  grey_frame = rgb2gray(frames);

  Z = uint8(abs(frame_1 - frames));
  grey_Z = rgb2gray(Z);
  imwrite(grey_Z, fullfile(Folder, sprintf('%06d.jpg', n)));
  n = n+1;
  frame_1 = frames;
  
  [idx,C] = kmeans(grey_Z(:),clusters, 'Start',locs);
  final = reshape(idx, size(grey_Z));
  output_img = mat2gray(final);
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
imshow(output_img , 'InitialMagnsification', 'fit');
hold on
scatter(mean_1(:,2), mean_1(:,1), 'r');
scatter(mean_2(:,2), mean_2(:,1), 'b', 'Marker', '*');
scatter(mean_3(:,2), mean_3(:,1), 'g', 'Marker', 'x');
scatter(mean_4(:,2), mean_4(:,1), 'r', 'Marker' , 'o');
