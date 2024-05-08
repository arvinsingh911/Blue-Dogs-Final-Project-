def recommend_sizes():
    while True:
        try:
            weight = int(input('Enter your weight (in pounds): '))
            if weight <= 0:
                raise ValueError('Weight must be a positive number.')

            body_type = input('Enter your body type (Slim/Average/Muscular): ')
            if body_type.lower() not in ['slim', 'average', 'muscular']:
                raise ValueError('Invalid body type. Please enter "Slim", "Average", or "Muscular".')

            
            top_size = 'S' if weight < 150 else ('M' if weight < 180 else 'L+')
            pants_size = '28-30' if weight < 150 else ('31-33' if weight < 180 else '34-36+')
            shoe_size = '8' if weight < 150 else ('9' if weight < 180 else '10+')

            
            print(f'Based on your weight ({weight} lbs) and body type ({body_type}), you should wear:')
            print(f'Top Size: {top_size}')
            print(f'Pants Size: {pants_size}')
            print(f'Shoe Size: {shoe_size}')

            break  
        except ValueError as e:
            print(f'Error: {e}')
            continue

recommend_sizes()

def height_suggestions():
    """
    Suggests clothing styles, sizes, and accessories based on the user's height.
    Returns:
        str: A suggestion for clothing styles, sizes, and accessories based on height.
    """
    while True:
        try:
            height = int(input("Enter your height in inches: "))
            if height <= 0:
                raise ValueError("Height must be a positive integer.")

            suggestion = ""
            if height < 60:
                suggestion = "Petite sizes and shorter hemlines may be more flattering. Consider small accessories like dainty jewelry."
            elif 60 <= height < 65:
                suggestion = "Standard sizes and regular hemlines are likely suitable. Accessories of moderate size and length are versatile."
            elif 65 <= height < 70:
                suggestion = "Standard sizes and regular hemlines are likely suitable. Accessories of moderate size and length are versatile. For bottoms, consider petite or short lengths."
            elif 70 <= height < 75:
                suggestion = "Tall sizes and longer hemlines may provide a better fit. Bold accessories and statement pieces can complement your height."
            elif height >= 75:
                suggestion = "Tall sizes and longer hemlines may provide a better fit. Bold accessories and statement pieces can complement your height. For bottoms, consider tall lengths."

            return suggestion
        except ValueError as e:
            print(f'Error: {e}')
            
print(height_suggestions())