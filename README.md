
The goal is to bring the software carpentry shell and python lessons back to Cowboy.  


Basic instructions:

Log in to Cowboy.

Download the repository:  

(NOTE: you can also first fork this repo to your github and clone it from there -- then you can make changes, push to your repo and even submit a pull reqest back to this repo.)  

  `git clone https://github.com/HPC-classes/python-on-cowboy.git`

  `cd python-on-cowboy`

Submit the job script (we'll look at what it's doing while it's running).  You *may* want to check `showq` and if there are a lot of free nodes, change the queue in the submit script from `express` to `batch`.

  `qsub inflammation.pbs`

When the job finishes, you'll see a new file `inflammation.pbs.oJOBID` and a new directory `output`

Download the contents of the output directory to your local computer (Cyberduck (https://cyberduck.io/?l=en), filezilla, winscp or via command line.)



