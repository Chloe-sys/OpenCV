import cv2

# Load the input image
input_image_path = "assignment-001-given.jpg"
output_image_path_final = "assignment-001-result.jpg"

# Read the input image
image = cv2.imread(input_image_path)

# Adjusted rectangle coordinates for better fit to the license plate
top_left = (260, 195)  # Move left to touch the plate
bottom_right = (988, 923)  # Widen to match reference image

# Draw a thick green rectangle around the license plate
cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 8)

# Define the position for the text
text_position = (820, 170)  # Position text above the rectangle
font_scale = 10  # Increase the font scale for larger text



# Create a transparent text background using overlay
overlay = image.copy()
cv2.rectangle(overlay, (820, 190), (1260, 90), (0, 0, 0), -1)

# Apply transparency to the rectangle background
alpha = 0.5 # Fully transparent background for the text rectangle
cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

# Add green license plate text above the rectangle
cv2.putText(image, 'RAH972U', text_position, cv2.FONT_HERSHEY_SIMPLEX, 3.1, (0, 255, 0), 8)

# Save the final result image
cv2.imwrite(output_image_path_final, image)

# Display the image (Optional)
cv2.imshow('Updated Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
