#include <iostream>
#include <unordered_map>
#include <stdio.h>
using namespace std;

bool canConstruct(string ransom_note, string magazine){
	unordered_map <char, int> voc_ransom_note;
	unordered_map <char, int> voc_magazine;

	// build vocabulary from magazine
	for(auto letter : magazine){
		if(voc_magazine.find(letter) != voc_magazine.end()){
			//there exist letter so increase counter (value)
			voc_magazine[letter] += 1;
		}else{
			//there is a new letter
			voc_magazine.insert({letter,1});
		}
	}

	//build vocabulary from ransom_note
	for(auto letter : ransom_note){
		if(voc_ransom_note.find(letter) != voc_ransom_note.end()){
			//there exist letter so increase counter (value)
			voc_ransom_note[letter] += 1;
		}else{
			//there is a new letter
			voc_ransom_note.insert({letter,1});
		}
	}
	int count_letters = 0;
	// iterate first voc_ransom_note and check its counters
	for(const auto & rn_pair: voc_ransom_note){
		//seach current letter in magazine vocabulary
		if(voc_magazine.find(rn_pair.first) != voc_magazine.end()){
			if(voc_magazine[rn_pair.first] == rn_pair.second){
				count_letters++;			
			}else{
				cout << "letter:" << rn_pair.first << " has different counts: [" << voc_magazine[rn_pair.first] << "," << rn_pair.second << "]" << endl;
			}
		}else{
			cout << "no existe letra: " << rn_pair.first << endl;
		}
	}
	if(count_letters == voc_ransom_note.size()){
		return true;
	}else{
		return false;
	}


}

int main(){

	canConstruct("chtiris","christian");
}
