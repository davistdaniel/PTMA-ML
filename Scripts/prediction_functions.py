#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pickle
import numpy as np
from ase.io import read


# In[31]:


mbtr = pickle.load(open('Scripts/mbtr_object.pkl','rb'))

def predict_MBTR(model,xyz):
    
    '''
    Predicts g value from a PTMA polymer structure given as an xyz file using the MBTR-ETR-model.
    
    Input :
    model : Trained model
    xyz_file : Path to XYZ file
    
    
    '''
    
    structure = read(xyz)    
    struct_vector = mbtr.create(structure)
    struct_vector = np.atleast_2d(struct_vector)
    
    pred = model.predict(struct_vector)

    return pred




# In[32]:


atom_pairs = pickle.load(open('Scripts/DAD_atoms_pairs.pkl','rb'))  ## read all pairs bonded atoms indices in PTMA structure.
atom_triplets = pickle.load(open('Scripts/DAD_atoms_triplets.pkl','rb')) ## read all three atom sets which are in PTMA structure
atom_quads = pickle.load(open('Scripts/DAD_atoms_quads.pkl','rb')) ## read all four atom sets which are in PTMA structure



def generate_DAD(xyz):
    '''
    
    Generate DAD feature vectors from xyz file.
    
    '''
    atoms = read(xyz)  # This is an ASE atoms object.

    
    feature_vector = []
    
    distances = [atoms.get_distance(atom1, atom2) for atom1, atom2 in zip(atom_pairs[0], atom_pairs[1])]
    feature_vector.extend(distances)
    
    angles = [atoms.get_angle(atom[0], atom[1], atom[2]) for atom in atom_triplets]
    feature_vector.extend(angles)
    
    dihedrals = [atoms.get_dihedral(atom[0], atom[1], atom[2], atom[3]) for atom in atom_quads]
    feature_vector.extend(dihedrals)
    
    return np.array(feature_vector)


# In[28]:


def predict_DAD(model,xyz):
    
    '''
    Predicts g value from a PTMA polymer structure given as an xyz file using the DAD-ETR-model
    
    Input :
    model : Trained DAD model
    xyz_file : Path to XYZ file
    
    
    '''
    
    struct_vector = generate_DAD(xyz)
    struct_vector = np.atleast_2d(struct_vector)
    
    pred = model.predict(struct_vector)

    return pred





# In[ ]:




