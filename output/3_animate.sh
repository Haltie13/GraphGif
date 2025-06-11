#!/bin/bash
# Animation script for GraphGif algorithm visualization

# Check if ImageMagick is available
if ! command -v convert &> /dev/null; then
    echo "ImageMagick not found. Please install it to create animations."
    exit 1
fi

# Create animated GIF
convert -delay 100 3_step_*.png 3_animation.gif

echo "Animation created: 3_animation.gif"
