def format_name(f_name, l_name):
    # Capitalize the first letter of each name
    title_f_name = f_name.title()
    title_l_name = l_name.title()
    
    # Return the full name with the last name first
    return f"{title_l_name} {title_f_name}"

# Call the function and print the result
full_name = format_name('RashFORD', 'marcus')
print(full_name)