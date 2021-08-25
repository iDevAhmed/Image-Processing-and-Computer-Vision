function saliency = saliency_output(image, filter_size)
%Step 1
im = imread(image);
%Step 2/3
im_grey = rgb2gray(im);
im_grey = im2double(im_grey);
%Step 4
fft2_im = fft2(im_grey);
%Step 5
fft2_im_abs = abs(fft2_im);
%Step 6
log_img = log(fft2_im_abs);
%Step 7
%fft2_im(fft2_im_abs<1e-6) = 0;
phase_img = unwrap(angle(fft2_im));
%Step 8 
output_log_median = zeros(size(im_grey),class(im_grey));
 for m = filter_size : size(im_grey,1)-2
     for n = filter_size : size(im_grey,2)-2
         list = log_img(m-2:m+2,n-2:n+2);
         output_log_median(m,n) = median(list(:));
     end
 end

%Step 9
spectralresidue_img = log_img - output_log_median;
%Apply step 10
% The Amount of noise in filter size 7 is more than the amount of noise in median filter
% of size 50. 

%Step 11
spectral_phase = spectralresidue_img + phase_img*1i;
%Step 12
spectral_phase_exp = exp(spectral_phase);
%Step 13
inverse_img = ifft2(spectral_phase_exp);

%Step 14
inverse_img_abs = abs(inverse_img);

inverse_img_squared = inverse_img_abs.^2;
%Step 15
h = fspecial('disk', 15);
inverse_img_squared = imfilter(inverse_img_squared, h);
saliency = mat2gray(inverse_img_squared);

imshow(saliency);   

end