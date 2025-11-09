class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        for portion in path.split("/"):
            if portion == "..":
                if st:
                    st.pop()
            elif portion == "." or not portion:
                continue
            else:
                st.append(portion)
        return "/" + "/".join(st)