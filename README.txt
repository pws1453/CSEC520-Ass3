The dataset file contains two objects: 

(1) a folder containing feature files, and 

(2) a CSV file containing malware labels for the feature files. 

You will need to understand both to load the data into your program correctly.

Feature Files:

	The name of each feature file is the SHA256 hash of the sample.

	Each feature file is a new-line separated file in which each line in the file represents a feature that is present in the sample.

	Each feature descriptor contains two parts (separated by a ‘::’ substring). 

	The first part identifies the type of feature, while the second describes the feature itself.
	Ex.  api_call::android/content/Context;->setWallpaper  

CSV File:

	This file contains two columns and 5,561 rows. 

	The first column identifies the SHA256 hash of the sample (i.e. the feature file’s name).

	The second column identifies the malware family of the sample. 

	Each row describes one sample.

	This file describes only malware samples. 

	Any sample present in the dataset, but not listed in this CSV file should be labeled as benign.
