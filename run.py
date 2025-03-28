import os
import subprocess

def main():
    kp_dir = os.path.join('/workspace/data', 'keypoints')
    op_img_dir = os.path.join('/workspace/data', 'openpose_images')
    if not kp_dir or not op_img_dir:
        raise EnvironmentError("Please set both KEYPOINTS_DIR and OPENPOSE_IMAGES_DIR environment variables.")
    
    cmd = (
        "cd submodules/openpose && ./build/examples/openpose/openpose.bin "
        "--image_dir /workspace/data/images "
        f"--write_json {kp_dir} --face --hand --display 0 "
        f"--write_images {op_img_dir}"
    )
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout, result.stderr)

if __name__ == "__main__":
    main()