# Juice pair co-programming project

## Design Brief

Create a webpage that allows users to explore how US population differs between genders for a given state. 

This is a two person programming exercise. You can break up the work however you wish. There should be a separate front end and back end. Don’t do everything in one technology and leave the other person with nothing to do. 

If you need to reduce or change the functionality in the wireframe, you can do so. It’s better that you wind up with something that’s simple, looks good and works, than try something too ambitious that isn’t completed.
Dataset

There is one datafile available in the data/ directory.

	CENSUS_STATEAGESEX.csv

The CENSUS_STATEAGESEX file contains raw data that consists of three dimensions: STATE, SEX, and AGE and two measures POP2000 and POP2008. Here’s an example:

	STATE,SEX,AGE,POP2000,POP2008
	Alabama,M,0,30479,32055
	Alabama,M,1,29904,32321
	Alabama,M,2,30065,31789
	Alabama,M,3,29932,31371
	Alabama,M,4,30319,31164
	Alabama,M,5,31127,31049

For instance, the second data row means that Alabama had 29,904 one-year old boys in 2000 and 32,321 one year old boys in 2008.


## Ideas and Tips

* We use Twitter’s Bootstrap. 
* Think like an editor. There are several stories to tell with this data (how state populations have changed over time, how age distribution have changed over time, the differences between men and women). Don’t make a tool that can look at everything. Have an opinion and focus deeper on a limited question.
* Think like a perfectionist. It’s better to do one thing well than several things poorly.
* Consider a tornado chart or small multiples as a way of visualizing data clearly. 
* Performance doesn’t matter.

## Sample timing

	10 - technical setup (source control approach (Github?, Dropbox)
	15 - pick a wireframe, technical approach (bootstrap/angular vs templated pages), who is doing what? What do you have to agree on
	45 - coding separately
	50 - coding together, bring it all together