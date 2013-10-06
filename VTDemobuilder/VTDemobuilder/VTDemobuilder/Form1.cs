using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Xml;

namespace VTDemobuilder
{
    public partial class Form1 : Form
    {
        //Format
        /*
         * <xml>
         * <Xsize>10</Xsize>
         * <Ysize>10</Ysize>
         * <types> this is the types e.g. skin
         * <cell>
         *  <id>1</id>//the type
         *  <rad>10</rad>//the max amout of radiation this type can handel
         *  <colour>#FFFFFF</colour>//colour
         * </cell>
         * <data>
         * <cell>1</cell>
         * <cell>1</cell>
         * <cell>4</cell>
         * <cell>1</cell>
         * <cell>2</cell>
         * </data>
         * </xml
         */
        string XML = "";
        public Form1()
        {
            InitializeComponent();
        }
        public void Out()
        {
            XmlDocument xdoc = new XmlDocument();
            xdoc.LoadXml(XML);
            xdoc.Save("xml.xml");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            XML = "<xml>\n";
            //Set data such as size
            XML += "<Xsize>" + textBox1.Lines[0].Split(' ').Length + "</Xsize>\n";
            XML += "<Ysize>" + textBox1.Lines.Length + "</Ysize>\n";
            //Set The types
            XML += "<type>\n";
            for (int i = 0;i < dataGridView1.Rows.Count -1; ++i)
            {
                XML += "<celltype>\n";
                XML += "<id>" + dataGridView1.Rows[i].Cells[0].Value + "</id>\n";
                XML += "<name>" + dataGridView1.Rows[i].Cells[1].Value + "</name>\n";
                XML += "<rad>" + dataGridView1.Rows[i].Cells[2].Value + "</rad>\n";
                XML += "<colour>" + dataGridView1.Rows[i].Cells[3].Value + "</colour>\n";
                XML += "</celltype>\n";
            }
            XML += "</type>\n";
            //Get Data
            XML += "<data>\n";
            for (int i = 0;i < textBox1.Lines.Length; ++i)//each line
            {
                string[] Line = textBox1.Lines[i].Split(' ');
                for (int l = 0; l < Line.Length;++l)//each number
                {
                    XML += "<cell>" + Line[l] + "</cell>\n";
                }
            }
            XML += "</data>\n";
            XML += "</xml>";
            Out();
        }
    }
}
