vidObj = VideoReader('Simple_bouncing_balls.mp4');
numFrames = ceil(vidObj.FrameRate*vidObj.Duration);

Folder = 'C:\Users\amjad\OneDrive\Desktop\Mini_Project_1_AML\MP1\videoFrames';

n = 1;
while hasFrame(vidObj)
  frames = readFrame(vidObj, 'native');
  grey_frame = rgb2gray(frames);
  imwrite(grey_frame, fullfile(Folder, sprintf('%06d.jpg', n)));
  n = n+1;
end 
