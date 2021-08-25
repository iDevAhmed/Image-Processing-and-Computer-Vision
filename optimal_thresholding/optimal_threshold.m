function final_output = optimal_threshold(im)
im = grey_scale(im, 3);
[height, width] = size(im);

pixel_topleft = im(1,1);
pixel_topright = im(1,width);
pixel_botleft = im(height,1);
pixel_botright = im(height,width);

%disp(pixel_topleft);
%disp(pixel_topright);
%disp(pixel_botleft);
%disp(pixel_botright);

bg_array = [pixel_topleft, pixel_topright, pixel_botleft,pixel_botright];
mask = ones(size(im),class(im));
mask(1,1) = 0;
mask(1,width) = 0;
mask(height,1) = 0;
mask(height,width) = 0;

fg_array = double(im) .* double(mask);

fg_array = nonzeros(fg_array);
disp(size(fg_array));
bg_array_mean = 0;
fg_array_mean = 0;

index_fg = 1;
index_bg = 1;
threshold = 0;
new_threshold = 1;
for index = 1:numel((fg_array))
    fg_array_mean = fg_array_mean + fg_array(index);
end

%BG Array Mean
for index = 1:numel((bg_array))
    bg_array_mean = bg_array_mean + bg_array(index);
end

fg_array_mean = fg_array_mean / numel(fg_array);
bg_array_mean = bg_array_mean / numel(bg_array);
threshold = (bg_array_mean + fg_array_mean) / 2;

% WHILE LOOP
while threshold ~= new_threshold
    for index = 1:numel((im))
        if im(index) > threshold
            fg_array(index_fg) = im(index);
            index_fg = index_fg + 1;
        else
            bg_array(index_bg) = im(index);
            index_bg = index_bg + 1;
        end
    end
    
       %FG Array Mean
for index = 1:numel((fg_array))
    fg_array_mean = fg_array_mean + fg_array(index);
end

%BG Array Mean
for index = 1:numel((bg_array))
    bg_array_mean = bg_array_mean + bg_array(index);
end

fg_array_mean = fg_array_mean / numel(fg_array);
bg_array_mean = bg_array_mean / numel(bg_array);
new_threshold = (bg_array_mean + fg_array_mean) / 2;

disp("Old Threshold");
disp(threshold);

disp("New Threshold");
disp(new_threshold);
end

end