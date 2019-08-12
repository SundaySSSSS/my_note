# msgpack C#
``` C#
using MsgPack.Serialization;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace msgpack_test
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            TestObj obj = new TestObj();
            obj.list.Add(new InnerObj { aa = 1, bb = 2});

            obj.table.Add(1, new InnerObj { aa = 3, bb = 4 });

            var serializer = MessagePackSerializer.Get<TestObj>();
            Stream stream = new MemoryStream();
            // Pack obj to stream.
            serializer.Pack(stream, obj);
            // Unpack from stream.
            stream.Position = 0;
            var unpackedObject = serializer.Unpack(stream);
            Console.WriteLine("a = " + unpackedObject.a);
            Console.WriteLine("b = " + unpackedObject.b);
            Console.WriteLine(obj.list.FirstOrDefault());
            Console.WriteLine(obj.table.FirstOrDefault());
        }

    }

    public class InnerObj
    {
        public int aa;
        public int bb;
    }
    public class TestObj
    {
        public int a;
        public int b;
        public double c;
        public List<InnerObj> list;
        public Dictionary<int, InnerObj> table;
        public Byte[] bytearray;

        public TestObj()
        {
            a = 1;
            b = 2;
            list = new List<InnerObj>();
            table = new Dictionary<int, InnerObj>();
            bytearray = new Byte[123];
            bytearray[0] = 9;
            //ArrayList
        }
};
}

```