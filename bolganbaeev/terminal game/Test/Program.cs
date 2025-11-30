using System;
using System.Threading;

// Класс ішінде жақсырақ, бірақ қарапайым C# файлы үшін осылай да жұмыс істейді
public class ConsoleGame
{
    public static void Main(string[] args)
    {
        // ===================================
        // 1. Айнымалыларды инициализациялау
        // ===================================
        int x = 2;       // Ойыншының x координатасы
        int y = 2;       // Ойыншының y координатасы
        int xb = 6;      // Нысананың x координатасы
        int yb = 2;      // Нысананың y координатасы
        int point = 0;   // Ұпай
        
        // Ойын алаңы (4 жол, 32 баған)
        int[][] matrix = new int[][]
        {
            new int[] {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 0, 0, 0, 1},
            new int[] {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 0, 0, 0, 1},
            new int[] {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 0, 0, 0, 1},
            new int[] {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 0, 0, 0, 1}
        };

        // Random нысанын циклден тыс жариялаймыз
        Random rand = new Random(); 

        bool running = true;
        
        Console.CursorVisible = false; // Курсорды жасыру
        
        // ===================================
        // 2. Негізгі ойын циклі
        // ===================================
        while (running)
        {
            // Ойыншы мен нысананы матрицада белгілеу
            matrix[y][x] = 2;
            matrix[yb][xb] = 3;

            // Экранды тазалау және басып шығару
            Console.Clear(); 
            for (int i = 0; i < matrix.Length; i++)
            {
                for (int o = 0; o < matrix[i].Length; o++)
                {
                    switch (matrix[i][o])
                    {
                        case 0: Console.Write(" "); break;
                        case 1: Console.Write("|"); break; // Қабырға
                        case 2: Console.Write("O"); break; // Ойыншы
                        case 3: Console.Write("$"); break; // Нысана
                    }
                }
                Console.WriteLine();
            }

            Console.WriteLine();
            Console.WriteLine("Your point: " + point);
            Console.WriteLine("Press ESC to exit.");
            
            // ===================================
            // 3. Пернелерді өңдеу және соқтығысуды тексеру
            // ===================================
            if (Console.KeyAvailable)
            {
                ConsoleKeyInfo key = Console.ReadKey(true);
                
                // Ойыншының ескі орнын тазалау
                matrix[y][x] = 0; 
                
                switch (key.Key)
                {
                    case ConsoleKey.W: // Жоғары
                        if (y > 0) y -= 1; 
                        break;
                    case ConsoleKey.S: // Төмен
                        if (y < (matrix.Length - 1)) y += 1; 
                        break;
                    case ConsoleKey.A: // Солға
                        if (x > 1) x -= 1; // 1-ші бағаннан (қабырғадан) өтпеу
                        break;
                    case ConsoleKey.D: // Оңға
                        if (x < (matrix[y].Length - 2)) x += 1; // Соңғы бағаннан (қабырғадан) өтпеу
                        break;
                    case ConsoleKey.Escape:
                        running = false;
                        break;
                }

                // Соқтығысуды тексеру
                if(y == yb && x == xb)
                {
                    point++;
                    
                    // Нысанаға жаңа кездейсоқ орын беру
                    // y: 0-ден matrix.Length-1-ге дейін
                    yb = rand.Next(0, matrix.Length); 
                    // x: 1-ден matrix[0].Length-2-ге дейін (қабырғалардың ішінде)
                    xb = rand.Next(1, matrix[0].Length - 1); 
                }
            }
            
            // 20 мс кідіріс (1000 / 50 = 20)
            Thread.Sleep(1000 / 60); 
        } 
        
        // ===================================
        // 4. Шығу
        // ===================================
        Console.CursorVisible = true; // Курсорды қайта қосу
        Console.Clear();
        Console.WriteLine("Ойын аяқталды. Жалпы ұпайыңыз: " + point);
        Console.WriteLine("Шығу үшін кез келген пернені басыңыз...");
        Console.ReadKey(true);
    }
}