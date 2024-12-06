

def part1 (s: str) -> int: 
    
    st = set()
    
    # st.add(s[:i] + (h1 if s[i] == "H" else o if s[i] == "O" else s[i]) + s[i+1:] for i in range(len(s)))
    
    st.update(s[:i] + x + s[i+1:]
              for i in range(len(s))
              for x in ["HO", "OH", "HH"]
              if (s[i] == "H" and x in ["HO", "OH"]) or 
              (x == "HH" and s[i] == "O"))

    # st.update(s[:i] + "HO" + s[i+1:] for i in range(len(s)) if s[i] == "H")
    # st.update(s[:i] + "OH" + s[i+1:] for i in range(len(s)) if s[i] == "H")
    # st.update(s[:i] + "HH" + s[i+1:] for i in range(len(s)) if s[i] == "O")
    
    return len(st)
 

if __name__ == "__main__": 
    print("Base: ", part1("HOH"))