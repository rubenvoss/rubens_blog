### Adding Custom Commands to Your Shell Configuration

Adding custom functions to your shell configuration files like `.bashrc` or `.zshrc` can significantly streamline your workflow. Here's a quick guide on how to add a custom command to convert screen recordings to YouTube-friendly formats using a script and the `ffpb` tool.

#### Step-by-Step Guide

1. **Open Your Shell Configuration File:**
   - For Bash, open `.bashrc`:
     ```sh
     nano ~/.bashrc
     ```
   - For Zsh, open `.zshrc`:
     ```sh
     nano ~/.zshrc
     ```

2. **Add the Custom Function:**
   Append the following function to the end of the file:
   ```sh
   # Converting Mac M1 screen recording to YouTube format
   youtube-converter() {
     if [[ $# -eq 0 ]] ; then
       echo 'Usage: youtube-converter input.mov output.mp4'
       return 1
     fi
     source /Users/user/code/ffpb-venv/bin/activate && ffpb -i "$1" -c:v libx264 -preset slow -crf 18 -c:a aac -ar 48000 -ac 2 -b:a 320k -profile:v high -level 4.0 -bf 2 -coder 1 -pix_fmt yuv420p -b:v 15M -threads 8 -cpu-used 0 -r 60 "$2"
   }
   ```

3. **Save and Close the File:**
   - Press `CTRL + X`, then `Y`, and hit `Enter` to save the changes.

4. **Reload the Configuration File:**
   - For Bash:
     ```sh
     source ~/.bashrc
     ```
   - For Zsh:
     ```sh
     source ~/.zshrc
     ```

### Using the `youtube-converter` Command

Once you have added the function to your shell configuration and reloaded it, you can easily convert your screen recordings. Here's how:

1. **Record Your Screen with QuickTime:**
   - Save the recording as `input.mov`.

2. **Convert the Recording:**
   - Use the `youtube-converter` function to convert the `.mov` file to `.mp4`:
     ```sh
     youtube-converter input.mov output.mp4
     ```

### How the Conversion Works

The `youtube-converter` function utilizes `ffpb`, a simple and fast FFmpeg front-end. It activates a Python virtual environment where `ffpb` is installed, and then executes the conversion command with the specified parameters.

**Command Breakdown:**
- `-i "$1"`: Specifies the input file.
- `-c:v libx264`: Uses the H.264 codec for video.
- `-preset slow`: Sets the compression preset.
- `-crf 18`: Controls the quality of the output video.
- `-c:a aac`: Uses the AAC codec for audio.
- `-ar 48000`: Sets the audio sampling rate.
- `-ac 2`: Specifies two audio channels (stereo).
- `-b:a 320k`: Sets the audio bitrate.
- `-profile:v high`: Uses the high profile for H.264.
- `-level 4.0`: Sets the level to 4.0.
- `-bf 2`: Uses two B-frames.
- `-coder 1`: Enables CABAC entropy coding.
- `-pix_fmt yuv420p`: Sets the pixel format.
- `-b:v 15M`: Sets the video bitrate.
- `-threads 8`: Utilizes 8 CPU threads.
- `-cpu-used 0`: Optimizes CPU usage.
- `-r 60`: Sets the frame rate to 60 fps.

By following these steps, you can efficiently convert QuickTime screen recordings to a YouTube-compatible format directly from your terminal. This method is particularly useful for Mac M1 users looking for a streamlined workflow.