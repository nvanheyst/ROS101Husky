# General notes
- Practising publishers and subscribers
- Initially tried sending velocity commands over specific time intervals to get distance, but this was very innacurate
- Implemented updated programs with odometry feedback for linear travel and rotation and got better results, but accuracy could still be improved for future programs
- Noticing an odd behaviour where initial set of twist messages is ignored, need to look into this further

# File list

- odometry_feedback_test.py 			          tests driving lin linear X using odometry feedback
- odometry_feedback_test_angular.py         tests rotations about Z using odometry feedback
- odometry_subscriber.py		 	              a simple subscriber to get odometry for debugging

# Archive


- instructionsforcomandsandintervals.txt  	contains instructions that I was trying to follow
- driving_command_interval.py 			        is the original with velocity commands over time
