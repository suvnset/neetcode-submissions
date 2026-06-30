class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}
        
        # loops through each string
        for word in strs:
            # initializes list corresponding to letters
            letter_list = [0] * 26
            
            # increments the frequency of a letter in the list
            for char in word:
                # converts letter to int
                index = ord(char.lower()) - 97
                letter_list[index] += 1

            letter_tuple = tuple(letter_list)
            
            # uses list as the key and the string as the value
            if letter_tuple not in anagrams_dict:
                anagrams_dict[letter_tuple] = [word]
            else:
                anagrams_dict[letter_tuple].append(word)

        return list(anagrams_dict.values())