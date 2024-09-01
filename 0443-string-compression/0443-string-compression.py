class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        # edge case if chars in size of 1
        if n == 1:
            return 1

        # setting iterators
        s_group = 0     # where the group start
        e_group = 1     # where the group end
        index = 0       # where to write the group letter and size
        size_group = 1  # size of group
        while e_group <= n:
            # count how many variables have in group
            if e_group < n and chars[s_group] == chars[e_group]:
                e_group += 1
                size_group += 1
            else:
                # write the compressed chars by algorithm conditions
                # write the letter of group
                chars[index] = chars[s_group]
                index += 1
                if size_group > 1:
                    """
                    # write the size of group
                    size_lst = list(str(size_group))
                    i_size = 0  # iterator of size list
                    for i in range(index, index + len(size_lst)):
                        chars[i] = size_lst[i_size]
                        i_size += 1
                        index += 1
                    """
                    # Write the count if greater than 1
                    size_group = e_group - s_group
                    if size_group > 1:
                        for c in str(size_group):
                            chars[index] = c
                            index += 1

                # setting iterators
                s_group = e_group
                e_group += 1
                size_group = 1

        # remove extra elements
        for i in range(n-1, index-1, -1):
            chars.pop()

        return len(chars)


                    