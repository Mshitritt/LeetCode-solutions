class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        # Group points by x-coordinate
        x_map = defaultdict(list)
        for x, y in points:
            x_map[x].append(y)

        # Dictionary to store previous y-pairs and their x-coordinates
        seen = {}
        res = float('inf')

        # Iterate through x-coordinates in sorted order
        for x in sorted(x_map):
            y_list = sorted(x_map[x])  # Sort y-coordinates for this x

            # Check all pairs of y-coordinates
            for i in range(len(y_list)):
                for j in range(i + 1, len(y_list)):
                    y1, y2 = y_list[i], y_list[j]

                    # If this y-pair has been seen before, calculate the rectangle area
                    if (y1, y2) in seen:
                        prev_x = seen[(y1, y2)]
                        res = min(res, (x - prev_x) * (y2 - y1))

                    # Update the y-pair with the current x-coordinate
                    seen[(y1, y2)] = x

        return res if res != float('inf') else 0
        
        