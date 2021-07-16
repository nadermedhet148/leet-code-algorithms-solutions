class Solution:
    def simplifyPath(self, path: str) -> str:
        pathLevels = [""];
        splitedPath = path.split("/")
        for level in splitedPath :
            if(level == "" or level == "."):
                continue;
            if(level == ".."):
                if(len(pathLevels) == 1):
                    continue;
                pathLevels.pop()
            else:
                pathLevels.append(level)

        if(len(pathLevels) == 1):
            return "/"
        
        newPath = "/".join(pathLevels)
        return newPath

s = Solution()
print(
s.simplifyPath("/../")
)

print(
s.simplifyPath("/a/./b/../../c/")
)