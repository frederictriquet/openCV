def distance_from_a_to_b(a: int, b: int) -> [{'name': 'distance_in_x_axis'},{'name': 'distance_in_y_axis'},{'name': 'euclidean_distance'}]:
    return {
      'distance_in_x_axis': a+b,
      'distance_in_y_axis': a-b,
      'euclidean_distance': a*b,
    }


print(distance_from_a_to_b(3,4))