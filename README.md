# Motion-detector-with-pyhton
The objective of video tracking is to associate target objects in consecutive video frames. The association can be especially difficult when the objects are moving fast relative to the frame rate. Another situation that increases the complexity of the problem is when the tracked object changes orientation over time. For these situations video tracking systems usually employ a motion model which describes how the image of the target might change for different possible motions of the object. For this fish video what teacher gives us video compression, key frames are divided into macroblocks. The motion model is a disruption of a key frame, where each macroblock is translated by a motion vector given by the motion parameters. The image of deformable objects can be covered with a mesh, the motion of the object is defined by the position of the nodes of the mesh.
I follow this rule to detect fish:
1.Taking an initial set of object detections (such as an input set of bounding box coordinates)
2.Creating a unique ID for each of the initial detections
3.And then tracking each of the objects as they move around frames in a video, maintaining the assignment of unique IDs

Furthermore, object tracking allows us to apply a unique ID to each tracked object, making it possible for us to count unique objects in a video. Object tracking is paramount to building a person counter (which we’ll do later in this series).
An ideal object tracking algorithm will:
•	Only require the object detection phase once (i.e., when the object is initially detected)
•	Will be extremely fast — much faster than running the actual object detector itself
•	Be able to handle when the tracked object “disappears” or moves outside the boundaries of the video frame
•	Be robust to occlusion
•	Be able to pick up objects it has “lost” in between frames
Algorithm:
This is a tall order for any computer vision or image processing algorithm and there are a variety of tricks we can play to help improve our object trackers.
But before we can build such a robust method, we first need to study the fundamentals of object tracking.
To perform video tracking an algorithm analyzes sequential video frames and outputs the movement of targets between the frames. There are a variety of algorithms, each having strengths and weaknesses. Considering the intended use is important when choosing which algorithm to use. There are two major components of a visual tracking system: target representation and localization, as well as filtering and data association.
Kernel-based tracking (mean-shift tracking: an iterative localization procedure based on the maximization of a similarity measure (Bhattacharyya coefficient).
Contour tracking: detection of object boundary (e.g., active contours or Condensation algorithm). Contour tracking methods iteratively evolve an initial contour initialized from the previous frame to its new position in the current frame. This approach to contour tracking directly evolves the contour by minimizing the contour energy using gradient descent.
Filtering and data association is mostly a top-down process, r. The following are some common filtering algorithms:
Kalman filter: an optimal recursive Bayesian filter for linear functions subjected to Gaussian noise. It is an algorithm that uses a series of measurements observed over time, containing noise (random variations) and other inaccuracies, and produces estimates of unknown variables that tend to be more precise than those based on a single measurement alone. 
Particle filter: useful for sampling the underlying state-space distribution of nonlinear and non-Gaussian processes. 

