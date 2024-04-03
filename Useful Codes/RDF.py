
import numpy as np

def distance_pbc(bead1,bead2,boxlen):
	values = bead1 - bead2;
	unwrapped = values-boxlen*np.round(values/boxlen)
	r = np.sqrt(np.sum(unwrapped*unwrapped))
	return r


def getrdf(particles_xyz, N,boxlen, dr, maxr, dimensions: int):
	"""Get radial distribution function for a square (2D) or cubic (3D) box. 
	If 2D, still need to input Nx3 vector, just have z positions be equal to zero."""
	pi = np.pi
	nbins = maxr/dr
	volumes = np.zeros(nbins)
	counts = np.zeros(nbins)
	if dimensions == 3:
		for v in range(1,nbins+1):
			volumes[v] = 4/3*pi*(v*dr)**3 - 4/3*pi*((v-1)*dr)**3
	elif dimensions == 2:
		for v in range(1,nbins+1):
			volumes[v] = pi*(v*dr)**2 - pi*((v-1)*dr)**2
	else:
		assert False
	#Here I start the rdf calculation by going through every b beads and then finding the distance and counting them
	for i in range(1,N):
		for j in range((i+1),N+1):
			d = distance_pbc(particles_xyz[i,:], particles_xyz[j,:], boxlen)
			if d <= maxr:
				# Figure out which bin this distance goes into here
				bin_choice = np.ceil(d/dr) # This should put them in bin 1 if d is from 0 to 0.1, 2 if d is 0.2 to 0.3 etc, bin 1 corresponds to 0 distance (see r_values)
				counts[bin_choice] = counts[bin_choice] + 2; # Double count when j goes from i+1 to N. 	    

	#Dividing my counts by the bulk concentration, the volumes, and the # of particles
	#Normalize the bin counts and store in the RDF here
	bulk_density = (N)/(boxlen**dimensions)
	RDF_final = counts/(N*volumes*(bulk_density))
	r_values = np.linspace(0,maxr-dr,int(np.ceil(maxr/dr))) #r_values = [dr:dr:maxr]' - dr;
	return (r_values, RDF_final)





