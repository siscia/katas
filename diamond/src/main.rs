fn diamond(c: char) -> Vec<String> {
    let mut result = Vec::new();
    let difference = c as i8 - 'A' as i8;
    let mut point_a = String::new();
    for _i in 0..difference {
        point_a.push(' ');
    }
    point_a.push('A');
    for _i in 0..difference {
        point_a.push(' ');
    }
    result.push(point_a);
    for i in 1..=difference {
        let mut row = String::new();
        for _j in i..difference {
            row.push(' ');
        }
        let letter = ('A' as u8 + i as u8) as char;
        row.push(letter);
        row.push(' ');
        for _j in 1..i {
            row.push(' ');
        }
        for _j in 1..i {
            row.push(' ');
        }
        row.push(letter);
        for _j in i..difference {
            row.push(' ');
        }
        result.push(row);
    }

    let mut buffer = Vec::new();
    for i in result.iter() {
        buffer.push(i.clone());
    }
    for (i, row) in buffer.iter().rev().enumerate() {
        if i > 0 {
            result.push(row.to_string())
        }
    }

    result
}

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_a() {
        let solution = vec!["A"];
        assert_eq!(solution, diamond('A'));
    }

    #[test]
    fn test_b() {
        #[rustfmt::skip]
        let solution = vec![" A ", 
                            "B B", 
                            " A "];
        assert_eq!(solution, diamond('B'));
    }

    #[test]
    fn test_c() {
        #[rustfmt::skip]
        let solution = vec!["  A  ", 
                            " B B ", 
                            "C   C", 
                            " B B ", 
                            "  A  "];
        assert_eq!(solution, diamond('C'));
    }

    #[test]
    fn test_d() {
        #[rustfmt::skip]
        let solution = vec!["   A   ", 
                            "  B B  ", 
                            " C   C ", 
                            "D     D", 
                            " C   C ", 
                            "  B B  ", 
                            "   A   "];
        assert_eq!(solution, diamond('D'));
    }

    #[test]
    fn test_e() {
        #[rustfmt::skip]
        let solution = vec!["    A    ", 
                            "   B B   ", 
                            "  C   C  ", 
                            " D     D ", 
                            "E       E", 
                            " D     D ", 
                            "  C   C  ", 
                            "   B B   ", 
                            "    A    "];
        assert_eq!(solution, diamond('E'));
    }

    #[test]
    fn chars_differences() {
        assert_eq!(1, 'B' as i8 - 'A' as i8)
    }

}
